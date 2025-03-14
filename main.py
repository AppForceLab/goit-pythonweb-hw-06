from db.seed import seed
from queries.selections import  select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10

def main():
    print("Starting database seeding...")
    seed()
    print("Database seeded successfully!\n")

    print("Select 1:")
    print(select_1())
    print("\nSelect 2:")
    print(select_2(1))
    print("\nSelect 3:")
    print(select_3(1))
    print("\nSelect 4:")
    print(select_4())
    print("\nSelect 5:")
    print(select_5(1))
    print("\nSelect 6:")
    print(select_6(1))
    print("\nSelect 7:")
    print(select_7(1, 1))
    print("\nSelect 8:")
    print(select_8(1))
    print("\nSelect 9:")
    print(select_9(1))
    print("\nSelect 10:")
    print(select_10(1, 1))
    print("\n")
    print("All queries executed successfully!")

if __name__ == '__main__':
    main()