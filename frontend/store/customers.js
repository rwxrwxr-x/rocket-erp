import service from '../services/customer_service';
import user_token from '../services/api';

export const state = () => ({
    active_customers: {},
});

export const mutations = {
    SET_RESOURCE: (state, active_customers) => {
        state.active_customers = active_customers;
    }
};

export const actions = {
    active_customers({commit, dispatch}, params) {
        const token = this.$auth.getToken('local');
        return service.get_active(params, this.$axios, token)
            .then((customers) => {
                commit('SET_RESOURCE', customers);
            });
    }
};

export const getters = {
    active_customers: state => state.active_customers
};
