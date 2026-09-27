def judge(question, expects, answer, results)->bool:
    """
    q: give', expect: 'give'
    the expect is in the answer
    """
    return expects.lower().strip() in answer.lower()
    pass



def retrieve(question, results)->bool:

    return  any(expects.strip().lower() for chunk in results)

    