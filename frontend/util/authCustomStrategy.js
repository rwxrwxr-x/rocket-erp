import Jsona from 'jsona';
import LocalScheme from "@nuxtjs/auth/lib/schemes/local";

export default class CustomScheme extends LocalScheme {
    formatUser(user) {
        const dataFormatter = new Jsona()
        return dataFormatter.deserialize(user)
    }

    async fetchUser(endpoint) {
        if (this.options.tokenRequired && !this.$auth.getToken(this.name)) {
            return
        }

        if (!this.options.endpoint.user) {
            this.$auth.setUser({})
            return
        }

        const user = await this.$auth.requestWith(
            this.name,
            endpoint,
            this.options.endpoints.user
        )

        if (user) {
            Promise.resolve(this.formatUser(user)).then((formattedUser) => {
                this.$auth.setUser(formattedUser)
            })
        }
    }
}