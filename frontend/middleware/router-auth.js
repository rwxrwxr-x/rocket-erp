export default function ({ store, redirect, route }) {
    console.log(store.state.user)
    store.state.user != null && route.name === 'login' ? redirect('/') : ''
    store.state.user === null && route.name !== 'login' ? redirect('/') : ''
}