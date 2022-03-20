import React from "react";
import {Link, } from 'react-router-dom'

const TodoItem = ({item, deleteTodo}) => {
    return (
        <tr>
            <td>
                {item.title}
            </td>
            <td>
                {item.text}
            </td>
            <td>
                {item.date_create}
            </td>
            <td>
                {item.status}
            </td>
            <td>
                {item.user.id}
            </td>
            <td>
                <button onClick={()=>deleteTodo(item.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const TodoList = ({items, deleteTodo}) => {
    return (
        <div>
        <table>
            <tr>
                <th>
                    title
                </th>
                <th>
                    text
                </th>
                <th>
                    date_create
                </th>
                <th>
                    status
                </th>
                <th>
                    users
                </th>
            </tr>
            {items.map((item) => <TodoItem item={item} deleteTodo={deleteTodo} />)}
        </table>
        <Link to='/todo/create'>Create</Link>
        </div>
    )
}

export default TodoList