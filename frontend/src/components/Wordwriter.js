import React, { useState, useEffect } from 'react';

const Wordwriter = ({ text, delay }) => {
  const words = text.split(' ');
  const [displayedWords, setDisplayedWords] = useState([]);
  const [currentWordIndex, setCurrentWordIndex] = useState(0);

  useEffect(() => {
    let timeout;

    if (currentWordIndex < words.length) {
      timeout = setTimeout(() => {
        setDisplayedWords(prevWords => [...prevWords, words[currentWordIndex]]);
        setCurrentWordIndex(prevIndex => prevIndex + 1);
      }, delay);
    }

    return () => clearTimeout(timeout);
  }, [currentWordIndex, delay, words]);

  return (
    <p>
      {displayedWords.map((word, index) => (
        <span key={index}>{word} </span>
      ))}
    </p>
  );
};

export default Wordwriter;
