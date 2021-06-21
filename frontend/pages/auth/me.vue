<template>
  <div class="container">
    <div class="mb-2 mt-4">
      <div>
        <ul class="nav nav-pills">
          <li class="nav-item hoverable">
            <span :class="[{ active: activeTab === 'profile' }, 'nav-link']"
              ><span @click="switchActiveTab('profile')">Account</span></span
            >
          </li>
          <li class="nav-item hoverable">
            <span :class="[{ active: activeTab === 'password' }, 'nav-link']"
              ><span @click="switchActiveTab('password')"
                >Change Password</span
              ></span
            >
          </li>
          <li v-if="loggedInUser.role === 'Member'" class="nav-item hoverable">
            <span :class="[{ active: activeTab === 'next-of-kin' }, 'nav-link']"
              ><span @click="switchActiveTab('next-of-kin')"
                >Next of kin</span
              ></span
            >
          </li>
        </ul>
      </div>
    </div>
    <hr />

  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  middleware: 'auth',
  data() {
    return {
      activeTab: 'profile',
      nextOfKin: []
    }
  },
  computed: {
    ...mapGetters({
      loggedInUser: 'loggedInUser'
    })
  },
  created() {
    this.retrieveNOK()
  },
  methods: {
    switchActiveTab(tab) {
      this.activeTab = tab
    },
    async retrieveNOK() {
      try {
        await this.$axios.get('users/members/next-of-kin/').then((response) => {
          if (response.status === 200) {
            this.nextOfKin = []
            const data = response.data
            if (data.length > 0) {
              data.forEach((element) => {
                this.nextOfKin.push({
                  firstName: element.first_name,
                  lastName: element.last_name,
                  phone: element.phone_number
                })
              })
            }
          }
        })
      } catch (e) {
        this.$toast.error('Could not retrieve next of kin')
      }
    }
  }
}
</script>