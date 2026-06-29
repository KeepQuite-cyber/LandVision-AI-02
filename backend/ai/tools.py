from plot.services import PlotService


class AITools:

    @staticmethod
    def execute(intent):

        action = intent.get("action")

        if action == "search_plot":
            return AITools.search_plot(
                intent.get("plot_number")
            )

        if action == "owner_details":
            return AITools.owner_details(
                intent.get("plot_number")
            )

        if action == "village_summary":
            return AITools.village_summary(
                intent.get("village")
            )

        if action == "filter_land_use":
            return AITools.filter_land_use(
                intent.get("land_use")
            )

        if action == "statistics":
            return AITools.statistics()

        return {
            "reply": "Sorry, I couldn't understand your request."
        }

    @staticmethod
    def search_plot(plot_number):

        plots = PlotService.get_by_plot_number(
            plot_number
        )

        if not plots.exists():

            return {
                "reply": f"Plot {plot_number} was not found."
            }

        plot = plots.first()

        return {

            "reply":
                f"Plot {plot.plot_number} found successfully.",

            "action":
                "highlight_plot",

            "plot_number":
                plot.plot_number,

            "plot_id":
                plot.id

        }

    @staticmethod
    def owner_details(plot_number):

        plots = PlotService.get_by_plot_number(
            plot_number
        )

        if not plots.exists():

            return {
                "reply":
                    f"Plot {plot_number} does not exist."
            }

        plot = plots.first()

        owner = plot.owner

        return {

            "reply":
                (
                    f"Plot {plot.plot_number} belongs to "
                    f"{owner.name}. "
                    f"It is a {plot.land_use} plot "
                    f"with an area of {plot.area} sq.m."
                ),

            "action":
                "highlight_plot",

            "plot_number":
                plot.plot_number,

            "plot_id":
                plot.id

        }

    @staticmethod
    def village_summary(village_name):

        plots = PlotService.search(
            village_name
        )

        if not plots.exists():

            return {

                "reply":
                    f"No village named {village_name} was found."

            }

        village = plots.first().village

        village_plots = PlotService.get_by_village(
            village.id
        )

        return {

            "reply":
                (
                    f"{village.name} has "
                    f"{village_plots.count()} plots."
                ),

            "village":
                village.name

        }

    @staticmethod
    def filter_land_use(land_use):

        plots = PlotService.get_by_land_use(
            land_use
        )

        if not plots.exists():

            return {

                "reply":
                    f"No {land_use} plots found."

            }

        plot_numbers = list(

            plots.values_list(
                "plot_number",
                flat=True
            )

        )

        return {

            "reply":
                (
                    f"Found {plots.count()} "
                    f"{land_use} plots."
                ),

            "action":
                "highlight_multiple",

            "plots":
                plot_numbers

        }

    @staticmethod
    def statistics():

        stats = PlotService.statistics()

        return {

            "reply":
                (
                    f"There are {stats['total_plots']} plots. "
                    f"Agriculture: {stats['agriculture']}, "
                    f"Residential: {stats['residential']}, "
                    f"Commercial: {stats['commercial']}, "
                    f"Industrial: {stats['industrial']}."
                ),

            "statistics":
                stats

        }