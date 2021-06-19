<template>
  <div>
    <!-- Page content -->
    <div class="container mt--9 pb-5">
      <div class="row justify-content-center">
        <div class="col-lg-5 col-md-7">
          <div class="card">
            <div class="card-body">
              <div class="text-center text-muted mb-4">
                <small>Sign in</small>
              </div>
              <form class="needs-validation" @submit.prevent="handleSubmit()">
                <base-input
                  name="Email"
                  prepend-icon="ni ni-email-83"
                  placeholder="Email"
                  v-model="model.email"
                >
                </base-input>

                <base-input
                  class="mb-3"
                  name="Password"
                  prepend-icon="ni ni-lock-circle-open"
                  type="password"
                  placeholder="Password"
                  v-model="model.password"
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
  </div>
</template>
<script>
export default {
  layout: "starter",
  data() {
    return {
      model: {
          email: 'example@example.com',
          password: '0123456789'
      }
    };
  },
  methods: {
      handleSubmit() {
        alert('Your data: ' + JSON.stringify(this.model));
    },
  },
};
</script>