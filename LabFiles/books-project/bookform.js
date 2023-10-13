import React from 'react';

export default function BookForm() {
    return (
        <div id='book-form' >
            <h4>Book Form</h4>
            <form >
                <table><tbody>
                    <tr>
                        <td>Isbn:</td>
                        <td><input type={'text'} name={'isbn'} /></td>
                    </tr>
                    <tr>
                        <td>Title:</td>
                        <td><input type={'text'} name={'title'} /></td>
                    </tr>
                    <tr>
                        <td>Price:</td>
                        <td><input type={'number'} name={'price'} /></td>
                    </tr>
                </tbody></table>
                <input type={'button'} value="Cancel" />
                <input type={'button'} value="Save" />
                <input type={'button'} value="Delete" />
            </form>
        </div>
    )
}