import Jsona from 'jsona';
const jsona = new Jsona();
import routes  from './api';

const route = "/api/v1/customer/active";
const get_active = (params, axios, token) => {
    return axios.get( route, {headers: {
        Authorization: token
        }})
        .then(response => {
            return response.data;
        });
};


export default {
    get_active
};
