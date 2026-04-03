import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()

# =========================
# CONFIGURATION
# =========================

OPENAI_API_KEY = os.getenv("API_TOKEN2")
BASE_URL = "http://127.0.0.1:1234/v1"

HEADERS = {
    "HTTP-Referer": "https://your-site.com",
    "X-Title": "LangChain Advanced LCEL Demo"
}

llm = ChatOpenAI(
    model="nvidia/nemotron-3-nano-4b",
    api_key=OPENAI_API_KEY,
    base_url=BASE_URL,
    default_headers=HEADERS,
    temperature=0.7,
    max_tokens=500
)

parser = StrOutputParser()

# =========================
# HELPER FUNCTION
# =========================

def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# =========================
# 1) SEQUENTIAL CHAIN
# Topic -> Blog Title -> Blog Content
# =========================

def run_sequential_chain(topic):
    print_section("1) SEQUENTIAL CHAIN: Topic -> Blog Title -> Blog Content")

    title_prompt = PromptTemplate.from_template(
        "Generate a catchy blog title for: {topic}"
    )

    content_prompt = PromptTemplate.from_template(
        "Write a short blog article using this title: {input}"
    )

    chain = (
        title_prompt
        | llm
        | parser
        | content_prompt
        | llm
        | parser
    )

    result = chain.invoke({"topic": topic})
    print(result)


# =========================
# 2) MULTI-STEP PIPELINE
# Topic -> Keywords -> Outline -> Full Article
# =========================

def run_seo_blog_pipeline(topic):
    print_section("2) MULTI-STEP PIPELINE: Topic -> Keywords -> Outline -> Full Article")

    chain = (
        PromptTemplate.from_template(
            "Generate SEO keywords for the topic: {topic}"
        )
        | llm
        | parser
        | PromptTemplate.from_template(
            "Create a blog outline using these keywords:\n{input}"
        )
        | llm
        | parser
        | PromptTemplate.from_template(
            "Write a detailed SEO-friendly blog article using this outline:\n{input}"
        )
        | llm
        | parser
    )

    result = chain.invoke({"topic": topic})
    print(result)


# =========================
# 3) PARALLEL / FAN-OUT CHAIN
# One Topic -> Tweet + LinkedIn + Instagram
# =========================

def run_social_media_generator(topic):
    print_section("3) PARALLEL CHAIN: Topic -> Tweet + LinkedIn + Instagram")

    tweet_chain = (
        PromptTemplate.from_template(
            "Write a short engaging tweet about: {topic}"
        )
        | llm
        | parser
    )

    linkedin_chain = (
        PromptTemplate.from_template(
            "Write a professional LinkedIn post about: {topic}"
        )
        | llm
        | parser
    )

    instagram_chain = (
        PromptTemplate.from_template(
            "Write a catchy Instagram caption about: {topic}"
        )
        | llm
        | parser
    )

    chain = RunnableParallel(
        tweet=tweet_chain,
        linkedin=linkedin_chain,
        instagram=instagram_chain
    )

    result = chain.invoke({"topic": topic})

    print("\nTweet:\n")
    print(result["tweet"])

    print("\nLinkedIn Post:\n")
    print(result["linkedin"])

    print("\nInstagram Caption:\n")
    print(result["instagram"])


# =========================
# 4) BONUS ADVANCED CHAIN
# Keep original topic + generate keywords
# Topic -> {topic + keywords} -> Blog
# =========================

def run_enriched_chain(topic):
    print_section("4) BONUS ENRICHED CHAIN: Keep Input + Add Generated Data")

    keyword_chain = (
        PromptTemplate.from_template(
            "Generate 5 important SEO keywords for the topic: {topic}"
        )
        | llm
        | parser
    )

    chain = (
        {
            "topic": RunnablePassthrough(),
            "keywords": keyword_chain
        }
        | PromptTemplate.from_template(
            "Write a blog introduction for topic: {topic}\n"
            "Use these keywords naturally: {keywords}"
        )
        | llm
        | parser
    )

    result = chain.invoke({"topic": topic})
    print(result)


# =========================
# MAIN PROGRAM
# =========================

if __name__ == "__main__":
    print_section("LANGCHAIN ADVANCED LCEL CHAINS DEMO")

    topic = input("Enter a topic: ").strip()

    if not topic:
        topic = "Kubernetes"

    run_sequential_chain(topic)
    run_seo_blog_pipeline(topic)
    run_social_media_generator(topic)
    run_enriched_chain(topic)