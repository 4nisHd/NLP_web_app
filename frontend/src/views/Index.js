import 'bootstrap/dist/css/bootstrap.css';
import Typewriter from 'components/Typewriter';
import { useState } from 'react';
import axios from 'axios';
import Wordwriter from 'components/Wordwriter';

const Index = () => {
  const [paragraph, setParagraph] = useState('');
  const [textData, setTextData] = useState(''); // State to store text data from the textarea

  const handleClick = async (button) => {
    try {
      console.log('Current Text Data:', textData);
      const response = await axios.post(
        'http://127.0.0.1:5000/api/text-summarization/',
        { buttonClick: button, textData },
        { headers: { 'Content-Type': 'application/json' } } // Specify Content-Type header
      );
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
          NLP.AI: <Typewriter text="الذكاء الصناعي في خدمة الغة العربية" delay={200} infinite />
        </h1>
      </div>
      <form>
        <div className="form-group w-50 mx-auto pt-9 text-center">
          <h1 className='text-center mb-5'>تلخيص النص</h1>
          <textarea
            placeholder='أدخل نص...'
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
            onClick={() => handleClick('summarize')}
          >
            تلخيص
          </button>
          <p className='pt-7 text-left font-weight-bold'><Wordwriter text={paragraph} delay={150} /></p> {/* Render the paragraph state using Wordwriter */}

        </div>
      </form>
    </div>
  );
};

export default Index;
