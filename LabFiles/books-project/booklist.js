import React from 'react';

export default function BookList() {
    return (<div id={'book-list'}>
        <h4>Book List</h4>
        <ul>
            <li>book one</li>
            <li>book two</li>
            <li>book three</li>
        </ul>
        <input type={'button'} value="New Book" />
    </div>
    );
}