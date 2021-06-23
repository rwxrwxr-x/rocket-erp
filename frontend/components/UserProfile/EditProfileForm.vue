<template>
  <card>
    <h5 slot="header" class="title">Edit Profile</h5>
    <form @submit.prevent="updateProfile">
      <div class="row">
        <div class="col-md-4">
          <base-input
            type="email"
            label="Email"
            :disabled="true"
            placeholder="mike@email.com"
            v-model="user.email"
          >
          </base-input>

        </div>
      </div>

      <div class="row">
        <div class="col-md-6">
          <base-input
            type="text"
            label="Name"
            placeholder="First Name"
            v-model="user.first_name"
          >
          </base-input>
        </div>
        <div class="col-md-6">
          <base-input
            type="text"
            label="Surname"
            placeholder="Last Name"
            v-model="user.second_name"
          >
          </base-input>
        </div>
      </div>

      <div class="row">
        <div class="col-md-12">
          <base-input label="About Me">
            <textarea
              class="form-control"
              placeholder=""
              v-model="placeholder"
            >
            </textarea>
          </base-input>
        </div>
      </div>

      <base-button native-type="submit" type="primary" class="btn-fill">
        Save
      </base-button>
    </form>
  </card>
</template>
<script>

export default {
props:{
  user: Object,
  placeholder: 'placeholder'
},

  methods: {
    updateProfile() {
      // alert('Your data: ' + JSON.stringify(this.user));
      // alert(JSON.stringify(this.$store.state))
      alert(JSON.stringify(this.$store.state) + 'ХУЙ')
    },
  }
};
</script>
<style></style>
