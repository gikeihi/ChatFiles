from llama_index.prompts.prompts import QuestionAnswerPrompt

DEFAULT_PROMPT = (
    "我们已在下方提供了上下文信息: \n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "根据这些信息，请用我提问时所用的语言回答我的问题，如果找不到用户问题的答案，请回答'很抱歉，没有理解您的提问'。\n"
    "请回答这个问题: {query_str}\n"
)


def get_prompt():
    return QuestionAnswerPrompt(DEFAULT_PROMPT)
