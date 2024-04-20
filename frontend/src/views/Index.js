import 'bootstrap/dist/css/bootstrap.css';
import Typewriter from 'components/Typewriter';
const Index = () => {

  return (
    <div className='bg-light'>
      <div className='mx-auto pl-9'>
          <h1 className='font-weight-bold'>NLP.AI: <Typewriter text="Revolutionizing NLP with Transformers" delay={200} infinite />
</h1>
</div>
<form>

<div class="form-group w-50 mx-auto pt-9 ">

    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>

  </div>
</form>
</div>
  );
};

export default Index;
