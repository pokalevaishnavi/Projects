import React from 'react';
import './index.css';
import avatar from './assets/avatar.png'; // Your princess-style image!

export default function App() {
  return (
    <div className="tangled-hero">
      <div className="lanterns"></div>

      {/* Avatar */}
      {/* <img src={avatar} alt="Vaishnavi Avatar" className="rapunzel-avatar" /> */}
      <div className="rapunzel-avatar-placeholder">Loading magic...</div>

      {/* Text */}
      <h1 className="fairy-headline">
        <span className="typing"> Hi, I’m Vaishnavi ✨</span>
      </h1>
      <p className="fairy-subtext">
        Web Dev 💻 | Tech Explorer 🤖
      </p>

      {/* Button */}
      <button className="fairy-cta">Enter My World</button>
    </div>
  );
}
