import Jsona from 'jsona';
const jsona = new Jsona();
import auth_routes  from './api';

const route = auth_routes.profile;
const get = (params, axios, token) => {
    return axios.get( route, {headers: {
        Authorization: token
        }})
        .then(response => {
            return response.data;
        });
};

const update = (profile, axios, token) => {
    const payload = jsona.serialize({
        stuff: profile,
        includeNames: []
    });

    return axios.patch(route, {headers: {
        Authorization: token}})
        .then(response => {
            return jsona.deserialize(response.data);
        });
};

export default {
    get,
    update
};