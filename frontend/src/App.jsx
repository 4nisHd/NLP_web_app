import { useState } from 'react';
import axios from 'axios';

function App() {
  const [paragraph, setParagraph] = useState('');

  const handleClick = async (button) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/get-paragraph', { buttonClick: button });
      setParagraph(response.data.paragraph);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <button onClick={() => handleClick('button1')}>Button 1</button>
      <button onClick={() => handleClick('button2')}>Button 2</button>
      <p>{paragraph}</p>
    </div>
  );
}

export default App;
