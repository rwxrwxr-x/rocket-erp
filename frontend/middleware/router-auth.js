export default function ({ store, redirect, route }) {
    store.state.user !== null && route.name === 'login' ? redirect('/') : ''
    store.state.user === null && route.name !== 'login' ? redirect('/') : ''
}