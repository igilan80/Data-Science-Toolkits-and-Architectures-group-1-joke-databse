from joke_operation import create_joke_table, add_joke, get_all_jokes, modify_joke, delete_joke, get_random_jokes


def main():

    # Create a joke table
    create_joke_table()

    # create random programming jokes
    random_jokes = get_random_jokes(2)

    db_joke_list = []

    # Add jokes to the table
    for joke in random_jokes:
        joke_data = add_joke(joke)
        db_joke_list.append(joke_data)

    # Modify a joke
    modify_joke(
        db_joke_list[0], "Why don't scientists trust atoms? Because they make up everything!")
    print("Updated jokes:", get_all_jokes())

    # Delete a joke
    delete_joke(db_joke_list[1])
    print("Jokes after deletion:", get_all_jokes())


if __name__ == "__main__":
    main()
