import turtle

def koch_snowflake(t, order, size):

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def main():

    try:
        recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return


    screen = turtle.Screen()
    screen.title("Сніжинка Коха")
    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(10)

    snowflake_turtle.penup()
    snowflake_turtle.goto(-150, 90)
    snowflake_turtle.pendown()

    for _ in range(3):
        koch_snowflake(snowflake_turtle, recursion_level, 300)
        snowflake_turtle.right(120)

    screen.exitonclick()

if __name__ == "__main__":
    main()
