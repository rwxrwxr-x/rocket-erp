import Jsona from 'jsona';
const jsona = new Jsona()
// const url = '127.0.0.1:8000'

function get(params, axios, token) {
    return axios.get( `/api/v1/auth/profile/`, {headers: {
        Authorization: token
        }})
        .then(response => {
            return response.data
            //     list: jsona.deserialize(response.data),
            //     // meta: response.data.meta
            // }k: response.data
        })
}

function update(profile, axios, token) {
    const payload = jsona.serialize({
        stuff: profile,
        includeNames: []
    });

    return axios.patch(`${url}/api/v1/auth/profile`, {headers: {
        Authorization: token}})
        .then(response => {
            return jsona.deserialize(response.data)
        })
}

export default {
    get,
    update
}