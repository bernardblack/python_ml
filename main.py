def DeepThought(question):

    if question == "The Ultimate Question of Life, the Universe, and Everything":
        return 42
    else:
        return "Do not bother me with little things"

def main():
    
    question = input("What do you want to know? : ")
    
    print(DeepThought(question))


if __name__ == "__main__":
    main()
