


def value_count(angry, disgust, fear, happy, sad, surprise, neutral):

    li = [len(angry), len(disgust), len(fear),
          len(happy), len(sad), len(surprise), len(neutral)]

    confidence_high = li[3] + li[-1] // sum(li)
    confidence_low = li[2] + li [4] // sum(li)

    if confidence_high > 75:

        print("Good confidence and Grade {}".format("Strong A++"))

        return "Good confidence and Grade {}".format("Strong A++")

    elif confidence_high < 74 or confidence_high >= 65:

        print("Better confidence and Grade {}".format("Strong A+"))

        return "Better confidence and Grade {}".format("Strong A+")

    elif confidence_high > 54 or  confidence_high < 64:

        print("its okay and Grade {}".format("weak B"))

        return "its okay and Grade {}".format("weak B")

    else:

        print("Need to improve and Grade {}".format("Failed"))

        return "Need to improve and Grade {}".format("Failed")
