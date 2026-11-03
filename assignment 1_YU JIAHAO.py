# ==========================================
# File Name: assignment 1_yourname.py
# Author: YU JIAHAO
# Student ID: 3036746442
# Date: 2026-11-03
# Description: Assignment 1 - Turtle Drawing & QA Bot
# ==========================================

import turtle

# ==========================================
# 任务一：Turtle Drawing
# ==========================================
def run_turtle_drawing():
    print("--- 启动 Turtle 绘图 ---")
    print("提示：绘图完成后，请点击弹出的绘图窗口以继续运行QA机器人。")
    
    screen = turtle.Screen()
    screen.bgcolor("black")  
    screen.title("HKU Assignment - Beautiful Colorful Pattern")
    
    t = turtle.Turtle()
    t.speed(0) 
    t.pensize(2)
    
    colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
    
    for i in range(60):    
        t.color(colors[i % len(colors)])    
        t.forward(i * 3) 
        t.pensize(i / 20 + 1)
        t.right(144)
        
    t.hideturtle()
    

    screen.exitonclick()
    print("--- 绘图结束 ---\n")

# ==========================================
# 任务二：QA Bot 
# ==========================================
def run_qa_bot():
    print("=" * 50)
    print("🤖 欢迎使用 QA Bot!")
    print("你可以向我询问关于以下关键词的问题：")
    print("HKU, robot, jetson, ai, human")
    print("输入 'exit' 或 'quit' 可以退出。")
    print("=" * 50)
    

    while True:

        user_input = input("\nYou: ").lower()
        
        if user_input in ["exit", "quit"]:
            print("Bot: 再见！很高兴为你服务。")
            break
            
        elif "hku" in user_input:
            print("Bot: HKU is The University of Hong Kong, a top-ranked university in Asia.")
        elif "robot" in user_input:
            print("Bot: Robots are machines capable of carrying out complex actions automatically.")
        elif "jetson" in user_input:
            print("Bot: NVIDIA Jetson is a series of embedded computing boards designed for AI and robotics.")
        elif "ai" in user_input:
            print("Bot: AI (Artificial Intelligence) is the simulation of human intelligence by machines.")
        elif "human" in user_input:
            print("Bot: Humans are amazing beings who created AI and Robots!")
        else:
            print("Bot: Sorry, I don't quite understand. Please ask me about HKU, robot, jetson, ai, or human.")


if __name__ == "__main__":
    run_turtle_drawing()
    run_qa_bot()
