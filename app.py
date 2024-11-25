from openai import OpenAI
import dotenv

dotenv_path = dotenv.find_dotenv()
APIKEY = dotenv.get_key(dotenv_path, "GPT_SECRET_KEY")  # .env 파일을 만들어 API 키관리
client = OpenAI(api_key=APIKEY)

# 1. 데이터셋 업로드
res = client.files.create(
  file=open("data/data_conversational.jsonl", "rb"),
  purpose="fine-tune"
)  # 내 데이터셋 을 openai 내 계정에 업로드

resId = res.id
print(f"trained file id : {resId}")

# 2. 파인튜닝 진행
response = client.fine_tuning.jobs.create(
  training_file=resId,  # 업로드된 나의 데이터셋을 아이디로 찾아 파인튜닝진행
  model="gpt-4o-mini-2024-07-18", 
  hyperparameters={
    "n_epochs":5,
    "batch_size": 1
  }
)