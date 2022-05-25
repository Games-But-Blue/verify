import discord 

class VerificationModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Get a unique code from [game]!", placeholder='Enter your verification code here!'))

    async def callback(self, interaction: discord.Interaction):
        code = self.children[0].value
        embed = discord.Embed(title="Modal Results")
        embed.add_field(name="Short Input", value=code)
        await interaction.response.send_message(embeds=[embed])