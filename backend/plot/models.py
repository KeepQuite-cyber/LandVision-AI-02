from django.db import models
from village.models import BaseModel, Village

class LandUse(models.TextChoices):
    AGRICULTURE = "Agriculture", "Agriculture"
    RESIDENTIAL = "Residential", "Residential"
    COMMERCIAL = "Commercial", "Commercial"
    INDUSTRIAL = "Industrial", "Industrial"
    GOVERNMENT = "Government", "Government"
    OTHERS = "Others", "Others"
class Owner(BaseModel):
    name = models.CharField(max_length=150, db_index=True)
    father_name = models.CharField(max_length=150, blank=True,null=True)
    mobile = models.CharField(max_length=10,blank=True,null=True )
    email = models.EmailField(blank=True,null=True)
    class Meta:
        db_table = "owners"
        ordering = ["name"]
        verbose_name = "Owner"
        verbose_name_plural = "Owners"

    def __str__(self):
        return self.name
class Plot(BaseModel):
    village = models.ForeignKey(Village,on_delete=models.CASCADE,related_name="plots")
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="plots")
    plot_number = models.CharField(max_length=50, db_index=True)
    area = models.DecimalField(max_digits=12,decimal_places=2,help_text="Area in Square Meter")
    land_use = models.CharField(max_length=30,choices=LandUse.choices,default=LandUse.AGRICULTURE)
    polygon = models.JSONField(help_text="Polygon Coordinates in GeoJSON format")
    remarks = models.TextField(blank=True,null=True)
    class Meta:
        db_table = "plots"
        ordering = ["plot_number"]
        verbose_name = "Plot"
        verbose_name_plural = "Plots"

        constraints = [
            models.UniqueConstraint(
                fields=["village", "plot_number"],
                name="unique_plot_per_village"
            )
        ]

        indexes = [
            models.Index(fields=["plot_number"]),
            models.Index(fields=["land_use"]),
        ]

    def __str__(self):
        return f"Plot {self.plot_number} - {self.village.name}"