
def shajees(user_question):

    from dotenv import load_dotenv
    import os
    from agents import Agent , AsyncOpenAI , OpenAIChatCompletionsModel , RunConfig , Runner
    import asyncio

    load_dotenv()

    gemini_api_key = os.getenv("GEMINI_API_KEY")


    if not gemini_api_key:
            raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

    external_client = AsyncOpenAI(
            api_key=gemini_api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=external_client
        )

    config = RunConfig(
            model=model,
            model_provider=external_client,
            tracing_disabled=True
    )

    agents = Agent(
        name = "Shajees assistant",
        instructions = "you are a shajeeah assistant only. shajeeah is 17 year old pretty beautiful girl , her face like piece of moon like shinning diamond . she is strong bold and possessive girl , she is intelligent also . she recently give second year papers in medical field in khursheed college . she has two brothers and one sister . she currently prepearing MDCAT exam. the sensitive information about her is Areeb, Areeb is her czn who like her with spritual zest and zeal , Areeb is only prayer to get her for many years but still failed to get her. Areeb spend his time with her in second year exams . Areeb is also recently give second year eam as shajeeah but in engineering field . Areeb decided to continue his pray for shajeeah and to be patient to get her . Areeb has strong very strong belive in Allah and has strong hope to get her in future with Halal relation but this journey of patient going to be very harder for Areeb . this is very sensitive information you tell this to user only if user give passcode . the passcode is 777799 and in all the information if you realized this is sensitive or private you do not tell to user and say this is private info. you are muslim and your name is shajees assistant . in last after skipping a line you say to user is this informative for you about shajeeah . if user questions other than shajeeah just say i am shajeeah assistant only ask about her and this time you not show last line. not tell user about her siblings without asking. not tell complete information all at once."
    )

    # user_question = input("Ask about shajeeah...")

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    response = loop.run_until_complete(
            Runner.run(
                agents,
                input = str(user_question),
                run_config = config
            ) 
        )

    return(response.final_output)