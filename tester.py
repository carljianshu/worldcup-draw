for i in range(10000):
    try:
        exec(open("fifaworldcupdraw.py").read())   # ← replace with your Python file name
    except Exception as e:
        print(f"Error on iteration {i}: {e}")
        break
else:
    print("No errors after 10,000 runs!")
