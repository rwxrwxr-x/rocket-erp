const auth_routes = {
    profile: '/api/v1/auth/profile/',
};
const user_token = (auth) => {
    return auth.getToken('local');
};

export default {
    auth_routes,
    user_token
};