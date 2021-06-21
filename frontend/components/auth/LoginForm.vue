  <template>
  <div class="container mt--9 pb-5">
      <div class="row justify-content-center">
        <div class="col-lg-5 col-md-7">
          <div class="card">
            <div class="card-body">
              <div class="text-center text-muted mb-4">
                <small>Sign in</small>
              </div>
              <form class="needs-validation" @submit="handleSubmit">
                <base-input
                  name="Email"
                  prepend-icon="ni ni-email-83"
                  placeholder="Email"
                  v-model="email"
                >
                </base-input>

                <base-input
                  class="mb-3"
                  name="Password"
                  prepend-icon="ni ni-lock-circle-open"
                  type="password"
                  placeholder="Password"
                  v-model="password"
                >
                </base-input>
                <div class="text-center">
                  <base-button type="primary" native-type="submit" class="my-4"
                    >Sign in</base-button
                  >
                </div>
              </form>
            </div>
          </div>
          <div class="row mt-3">
            <div class="col-6">
              <router-link to="/password/reset" class="text-light"
                ><small>Forgot password?</small></router-link
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>

<script>
// import { apiReq } from '~/plugins/misc-functions'
const Cookie = require('js-cookie')
export default {
  middleware: "noauth",
  data: () => ({
    email: "",
    password: "",
    error: null
  }),
  methods: {
    async handleSubmit(evt) {
      evt.preventDefault()
      let res = await this.$axios.$post(`http://localhost:8000/api/v1/auth/jwt`, { email: this.email, password: this.password});
      this.$store.commit('setAuth', { access: res.access, refresh: res.refresh })
      Cookie.set('access', res.access)
      this.$router.push('/')
      // 			evt.preventDefault()
			// var loginReq = await apiReq(this, 'api/v1/auth/jwt', { email: this.email,
			// 											password: this.password });
			// if (loginReq.status === 'error') {
			// 	if (loginReq.response.message != null && loginReq.response.message != '') {
			// 		this.errorMessage = loginReq.response.message
			// 	}
			// 	else {
			// 		this.errorMessage = 'Login failed. Please try again.'
			// 	}
			// 	this.showAlert = true
			// }
			// else if (loginReq.status === 200) {
			// 	await this.$store.dispatch('setState', { email: loginReq.response.email,
			// 										logged_in: true,
			// 										access: loginReq.response.access })
			// 	await this.$axios.setToken(loginReq.response.access)
			// 	this.$router.push('/')
			// }
    }
  }
}
</script>