import os
import openai
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


MD_DIR = Path(r"C:\work\chunking-doc\split_md")  
LOG_FILE = Path("upload_vectorstore_log.txt")
VECTOR_STORE_NAME = "rag"

def upload_file_to_openai(file_path: Path) -> str:
    with open(file_path, "rb") as f:
        response = openai.files.create(
            file=f,
            purpose="assistants"
        )
    return response.id

def create_vector_store(name=VECTOR_STORE_NAME) -> str:
    response = openai.vector_stores.create(name=name)
    print(f" Vector Store Created: {response.id}")
    return response.id

def attach_file_to_vector_store(vector_store_id: str, file_id: str):
    openai.vector_stores.files.create_and_poll(
        vector_store_id=vector_store_id,
        file_id=file_id
    )

def main():
    vector_store_id = create_vector_store()
    files = list(MD_DIR.glob("*.md"))

    total_uploaded = 0
    with LOG_FILE.open("w", encoding="utf-8") as log:
        log.write(f"Vector Store ID: {vector_store_id}\n")
        log.write("filename\tfile_id\n")

        for md_file in sorted(files):
            try:
                file_id = upload_file_to_openai(md_file)
                attach_file_to_vector_store(vector_store_id, file_id)
                log.write(f"{md_file.name}\t{file_id}\n")
                print(f" Uploaded & attached: {md_file.name} → file_id: {file_id}")
                total_uploaded += 1
            except Exception as e:
                print(f" Failed to process {md_file.name}: {e}")
    
    log.write(f"\nTotal files uploaded: {total_uploaded}\n")

    print(f"\n Total")
    print(f"  Markdown files uploaded: {total_uploaded}")
    print(f"  Vector Store ID: {vector_store_id}")
    print(f"  Log saved to: {LOG_FILE}")

if __name__ == "__main__":
    main()
