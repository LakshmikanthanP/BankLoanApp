import React from 'react';
import { useState } from "react";

  function LoanForm(props) {
  const [userName, setuserName] = useState("")
  const [yearEstablished, setyearEstablished] = useState("")
  const [loanAmount, setloanAmount] = useState("")
  const [balancesheetInfo,setbalancesheetInfo] = useState("")
  const [loanresult, setloanresult] = useState(); 
  const [profitlastyear,setprofitlastyear] = useState("")
  const [averageassets,setaverageassets] = useState("")


  const OnRequestBalanceSheet = (e) => {
      if (userName && yearEstablished && loanAmount) {
        const getrequestinfo = {
        businessdetails: { name: userName, year: yearEstablished, loanAmount: loanAmount},
        accountprovider: "Xerox"
      }
      fetch("http://mainservice:5000/balancesheet", {
        method: 'POST',
        headers: new Headers({
            'Access-Control-Allow-Origin': '*',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }),
        body: JSON.stringify(getrequestinfo)
        })
        .then(
            response => response.json())
        .then(data => {
            const dataarray = JSON.parse(data)
            console.log(dataarray)
            
            console.log(dataarray.profitLastYear)
            console.log(dataarray.netaverageassets)
            setaverageassets(dataarray.netaverageassets)
            setprofitlastyear(dataarray.profitLastYear)
            setbalancesheetInfo(data)           
             // setLoading(false);
             //setError(null);
        })
        .catch(error => {

            //setLoading(false);
            //setError('Something went wrong, please try again later.');
        });
      }
   }
   const loanrequesInfo = {
    businessdetails: { name: userName, year: yearEstablished},
    profitlastyear: profitlastyear,
    averageassets: averageassets,
    loanAmount: loanAmount,

  }
    const handleSubmit= (e) => {
      e.preventDefault();

  fetch("http://mainservice:5000/procesloan", {
    method: 'POST',
    headers: new Headers({
        'Access-Control-Allow-Origin': '*',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        
    }),
    body: JSON.stringify(loanrequesInfo)
    })
    .then(
        response => response.json())
    .then(data => {
        const dataarray = JSON.parse(data)
        console.log(dataarray)
        
        setloanresult(data)    
    })
    .catch(error => {

    });
}
  
    return (
        <form onSubmit={e => { handleSubmit(e); } }>
            <label><h1>Loan Application Form</h1></label>
            <br />
            <br />
            <label>Name</label>
            <br />
            <input
                name='userName'
                value={userName}
                onChange={(e) => setuserName(e.target.value)}
                type='text' />
            <br />
            <label>YearEstablished</label>
            <br />
            <input
                name='yearEstablished'
                value={yearEstablished}
                onChange={(e) => setyearEstablished(e.target.value)}
                type='date' />
            <br />
            <label>LoanAmount</label>
            <br />
            <input
                name='loanAmount'
                value={loanAmount}
                onChange={(e) => setloanAmount(e.target.value)}
                type='number' />
            <br />
            <label>
                Pick your acconting provider:
                <select >
                    <option value="Xerox">Xerox</option>
                    <option value="MYOB">MYOB</option>
                </select>
            </label>
            <div>
                <br></br>
                <br></br>
                <button type="button" onClick={OnRequestBalanceSheet}>
                    RequestBalanceSheet
                </button>
                <br></br>
                <br></br>
            </div>
            <div>
            <div>
            <label>profitLastYear</label>
            <input 
            name='profitlastyear'
            value={profitlastyear}
            >
            </input>
            <label>averageassets</label>
            <input name='averageassets'
                    value={averageassets}
                        >
            </input>
            <br></br>
            <br></br>
            </div>
            <label>Balance Sheet</label>
            <textarea
                rows = {30}
                name='balancesheetInfo'
                value={balancesheetInfo}
                type='text' />
            <br></br>
            <br></br>
            </div>
            <input
                className='submitButton'
                type='submit'
                disabled = {balancesheetInfo.length ==0}
                value='Submit' />
                        <div>
            <label>LoanOutcome</label>
                    <textarea
                    rows = {10}
                    value ={loanresult}
                    name='loanresult'
                    type='text' />
            </div>
        </form>
        

    )
  }

  export default LoanForm;