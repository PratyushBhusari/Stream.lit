import streamlit as st
from pydub import AudioSegment
from pydub.generators import WhiteNoise
import random
import io

def generate_crackle(duration_ms=5000):
    # Create a white noise sound
    noise = WhiteNoise().to_audio_segment(duration=duration_ms)
    
    # Generate crackle effect by adding random bursts of noise
    crackle = AudioSegment.silent(duration=duration_ms)
    
    for _ in range(duration_ms // 100):
        start = random.randint(0, duration_ms - 100)
        burst = noise[start:start+100]
        crackle = crackle.overlay(burst, position=start)
    
    return crackle

def main():
    st.title("Car Crackle Sound Generator")
    st.write("Click the button below to generate a car crackle sound.")
    
    if st.button("Generate Crackle Sound"):
        # Generate a crackle sound
        crackle_sound = generate_crackle()
        
        # Save the sound to a BytesIO object
        audio_bytes = io.BytesIO()
        crackle_sound.export(audio_bytes, format="wav")
        audio_bytes.seek(0)
        
        st.audio(audio_bytes, format="audio/wav")
        
        st.write("Crackle sound generated!")

if __name__ == "__main__":
    main()
