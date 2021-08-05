import React from "react";

const ProjectsItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.title}
            </td>
            <td>
                {item.link_rep}
            </td>
            <td>
                {item.users.email}
            </td>
        </tr>
    )
}

const ProjectsList = ({items}) => {
    return (
        <table>
            <th>
                title
            </th>
            <th>
                link_rep
            </th>
            <th>
                users
            </th>
            {items.map((item) => <ProjectsItem item={item} />)}
        </table>
    )
}

export default ProjectsList