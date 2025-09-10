import React from 'react';

function RequestForm() {
    return (
        <div style={{margin: "20px"}}>
            <h2>Submit a Request</h2>
            <form>
                <input type="text" placeholder="Name" /><br/>
                <input type="text" placeholder="Category" /><br/>
                <input type="text" placeholder="Description" /><br/>
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

export default RequestForm;
