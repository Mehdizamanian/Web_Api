
import './App.css';

import React, { useEffect, useState } from 'react';


function App() {
  const[books,SetBook]=useState([]);

  useEffect(()=>{
    fetch("http://127.0.0.1:8000/api/",{
      method:"GET",
      headers:{"Content-type":"application/json"}


    }).then(resp=>resp.json()).then(resp=>SetBook(resp)).catch(error=>console.log(error))
  },[])
 
  return (
    <div className="App">
      <header className="App-header">
       
        <h3>
          Full-Stack Web Application developed with Django & React 
        </h3>




        {books.map(book=>{
          return <h2 style={{color:"yellow"}}>{book.title}</h2>
        })}

      </header>
    </div>
  );
}

export default App;
