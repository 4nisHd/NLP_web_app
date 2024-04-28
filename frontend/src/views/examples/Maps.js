import 'bootstrap/dist/css/bootstrap.css';
import Typewriter from 'components/Typewriter';
import { useState } from 'react';
import axios from 'axios';
import Wordwriter from 'components/Wordwriter';

const Maps = () => {
  const [paragraph, setParagraph] = useState('');
  const [textData, setTextData] = useState(''); // State to store text data from the textarea

  const handleClick = async (button) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/text-summarization/', { buttonClick: button, textData });
      setParagraph(response.data.paragraph);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleTextareaChange = (event) => {
    setTextData(event.target.value); // Update the text data state as the user types in the textarea
  };

  return (
    <div className='bg-light'>
      <div className='bg-warning mx-auto pl-9'>
        <h1 className='font-weight-bold'>
          NLP.AI: <Typewriter text="Revolutionizing NLP with Transformers" delay={200} infinite />
        </h1>
      </div>
      <form>
        <div className="form-group w-50 mx-auto pt-9 text-center">
          <h1 className='text-center mb-5'>Text Summarization</h1>
          <textarea
            placeholder='Enter text...'
            className="form-control"
            id="exampleFormControlTextarea1"
            rows="6"
            value={textData} // Bind the value of the textarea to the textData state
            onChange={handleTextareaChange} // Call handleTextareaChange on textarea change
          ></textarea>
        </div>
        <div className="col-md-12 text-center">
          <button
            type="button"
            className="btn btn-warning"
            onClick={() => handleClick('summerize')}
          >
            Summarize
          </button>
        </div>
        <p>{paragraph}</p>
      </form>
    </div>
  );
};

export default Maps;
