const routes = {
    profile: '/api/v1/auth/profile',
    active_customers: '/api/v1/customer/active/'
};
const user_token = (auth) => {
    return auth.getToken('local');
};

export default {
    routes,
    user_token
};
