<template>
  <div class="row">
    <div class="col-md-8"><edit-profile-form :user="user"> </edit-profile-form></div>
    <div class="col-md-4"><user-card :user="user"> </user-card></div>
  </div>
</template>
<script>
import EditProfileForm from '../components/UserProfile/EditProfileForm.vue';
import UserCard from '../components/UserProfile/UserCard.vue';

export default {
  middleware: 'auth',
  name: 'user',

  components: {
    EditProfileForm,
    UserCard
  },
  data: () => {
    return {
      user: {
        type: 'profile',
        first_name: null,
        second_name: null,
        email: null
      }
    }
  },
  created () {
    this.getProfile()
  },
  methods: {
    async getProfile() {
      this.$store
      await this.$store.dispatch('profile/me')
      this.user = await {...this.$store.getters["profile/me"]}
    }
  },

};
</script>
<style></style>
