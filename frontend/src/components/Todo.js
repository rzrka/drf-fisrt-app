import React from "react";

const TodoItem = ({item}) => {
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
                {item.users.email}
            </td>
        </tr>
    )
}

const TodoList = ({items}) => {
    return (
        <table>
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
            {items.map((item) => <TodoItem item={item} />)}
        </table>
    )
}

export default TodoList