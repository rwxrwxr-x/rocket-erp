import Vuex from 'vuex'
import cookieparser from 'cookieparser'
import createPersistedState from 'vuex-persistedstate'


export const state = () => {
	return {
		access: null,
		refresh: null
	}
}

export const mutations = {
	setAuth (state, { access, refresh }){
		state.access = access
		state.refresh = refresh
	}
}

export const actions = {
	nuxtServerInit ({ commit }, { req }) {
		let access = null
		let refresh = null
		console.log('actions')
		if (req.headers.cookie) {
			const parsed = cookieparser.parse(req.headers.cookie)
			try {
				access = JSON.parse(parsed.auth)

			} catch (err) {
			}
		}
		commit('setAuth', {access, refresh})
	}
}