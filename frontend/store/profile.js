import service from '../services/profile_service';
import user_token from '../services/api';

export const state = () => ({
    me: {},
});

export const mutations = {
    SET_RESOURCE: (state, me) => {
        state.me = me;
    }
};

export const actions = {
    me({commit, dispatch}, params) {
        const token = this.$auth.getToken('local');
        return service.get(params, this.$axios, token)
            .then((profile) => {
                commit('SET_RESOURCE', profile.user);
            });
    },

    update({commit, dispatch}, params) {
        const token = user_token(this.$auth);
        return service.update(params, this.$axios, token)
            .then((profile) => {
                commit('SET_RESOURCE', profile);
            });
    }
};

export const getters = {
    me: state => state.me
};
