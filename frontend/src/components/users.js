import React from "react";

const UsersItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.email}
            </td>
            <td>
                {item.username}
            </td>
            <td>
                {item.first_name}
            </td>
            <td>
                {item.last_name}
            </td>
        </tr>
    )
}

const UsersList = ({items}) => {
    return (
        <table>
            <th>
                email
            </th>
            <th>
                username
            </th>
            <th>
                firstname
            </th>
            <th>
                lastname
            </th>
            {items.map((item) => <UsersItem item={item} />)}
        </table>
    )
}

export default UsersList