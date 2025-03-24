import streamlit as st
import random

def main():
    st.title("Guess the Number Game!")
    
    # Initialize session state variables
    if 'target' not in st.session_state:
        st.session_state.target = random.randint(1, 100)
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    
    st.write("Guess a number between 1 and 100!")
    
    # User input
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    
    if st.button("Submit Guess") and not st.session_state.game_over:
        st.session_state.attempts += 1
        if guess < st.session_state.target:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.target:
            st.warning("Too high! Try again.")
        else:
            st.success(f"Correct! You guessed the number in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True
    
    # Restart game button
    if st.session_state.game_over:
        if st.button("Play Again"):
            st.session_state.target = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.game_over = False

if __name__ == "__main__":
    main()
