export default function ({ store, redirect }) {
  // If the user is authenticated redirect to home page
  if (store.state.access) {
    console.log('YEP')
  }
  console.log(store.state)
  console.log(store.state.access)
  if (store.state.access) {
    return redirect(200, '/')
  }
}
