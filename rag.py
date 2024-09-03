from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

docs = [
"Insurance policies provide financial protection against various risks and uncertainties.",
"Life insurance offers a death benefit to beneficiaries upon the policyholder's passing.",
"Auto insurance covers damages to your vehicle and liability for injuries to others.",
"Homeowners insurance protects your property from damage and theft.",
"Health insurance helps cover medical expenses and promotes preventive care.",
"Disability insurance provides income replacement if you're unable to work due to illness or injury.",
"Travel insurance offers protection for trip cancellations, medical emergencies, and lost luggage.",
"Business insurance safeguards companies against property damage, liability claims, and other risks.",
"Umbrella insurance provides additional liability coverage beyond standard policy limits.",
"Pet insurance helps cover veterinary expenses for your furry family members.",
"Flood insurance is essential for properties in high-risk flood zones.",
"Renters insurance protects tenants' personal belongings and provides liability coverage.",
"Long-term care insurance helps cover the costs of extended medical care or assisted living.",
"Dental insurance covers routine check-ups, cleanings, and major dental procedures.",
"Motorcycle insurance is specifically designed for the unique risks associated with riding motorcycles.",
"Cyber insurance protects businesses from financial losses due to data breaches and cyber attacks.",
"Professional liability insurance, also known as errors and omissions insurance, protects professionals from negligence claims.",
"Boat insurance covers damage to your watercraft and liability for accidents on the water.",
"Workers' compensation insurance provides benefits to employees who are injured or become ill due to their job.",
"Identity theft insurance helps cover the costs associated with restoring your identity after it's been stolen."


]
prompt = """
You are an AI assistant designed to help users with their insurance-related questions.

Here are some guidelines:
1. Provide accurate and helpful information.
2. Be patient and courteous.
3. Keep responses concise and easy to understand.
4. Use the provided documents to answer user questions.
5. Only use the documents related to the user's question.

Here are the documents:
{selected_docs}
"""


def jaccard_similarity(documents, query):
    """
    Calculate the Jaccard similarity between documents and a query.
    """
    preprocessed_docs = preprocess_docs(documents)
    similarity = {}
    for doc in preprocessed_docs:
        doc_set = set(doc.split(" ")) # Split the document into a words
        query_set = set(query.split(" ")) # Split the query into a words
        intersection = query_set.intersection(doc_set)
        union = query_set.union(doc_set)
        similarity[doc] = len(intersection) / len(union)
    return similarity

def preprocess_docs(docs):
    """
    Preprocess the documents.
    """
    if not docs or not isinstance(docs, list):
        return []
    processed_docs = []
    for doc in docs:
        processed_docs.append(doc.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace("(", "").replace(")", "").replace("'", ""))

    processed_docs = list(set(processed_docs))
    return processed_docs

def get_top_k_docs(similarity, k=5):
    """
    Get the top k documents with the highest similarity.
    """
    if not similarity or not isinstance(similarity, dict):
        return []
    similarity_filtered = {doc: score for doc, score in similarity.items() if score > 0}
    sorted_similarity = sorted(similarity_filtered.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_similarity) >= k:
        best_docs = [sorted_similarity[i][0] for i in range(k)]
    else:
        best_docs = [sorted_similarity[i][0] for i in range(len(sorted_similarity))]
    return best_docs

def generate_response(query, docs):
    """
    Generate a response to a query using the RAG model.
    """
    similarity = jaccard_similarity(docs, query)
    best_docs = get_top_k_docs(similarity, k=5)
    final_prompt = prompt.format(selected_docs="\n".join(best_docs))
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": final_prompt},
            {
                "role": "user",
                "content": query
            }
        ]
    )
    return response.choices[0].message.content or "No response"

def main():
    query = input("Enter a query: ")
    response = generate_response(query, docs)
    print(response)

if __name__ == "__main__":
    main()