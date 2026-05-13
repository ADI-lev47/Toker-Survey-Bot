from toker_agent import run_whatsapp_bot

def main():
    print("--- ברוכה הבאה למחולל הסקרים של טוקר ---")
    
    while True:
        # קריאה לפונקציה שמייצרת ושולחת
        run_whatsapp_bot()
        
        # האפשרות ליצור סקר נוסף
        print("\n" + "="*30)
        choice = input("רוצה ליצור ולשלוח עוד סקר? (כן/לא): ").strip().lower()
        
        if choice not in ['כן', 'y', 'yes', 'k']:
            print("מסיימים... להתראות!")
            break

if __name__ == "__main__":
    main()
