from Search_Engine import *

def search_execute(api_key,question):
    loader = DirectoryLoader('./Store',glob='**/*.txt')
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    texts = text_splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(openai_api_key=api_key,model="text-embedding-ada-002")
    db = Chroma.from_documents(texts, embeddings)

    retriever = db.as_retriever()

    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever,return_source_documents=True)

    #question = input('Enter your question: ')
    output = qa(question)
    
    return output['result']