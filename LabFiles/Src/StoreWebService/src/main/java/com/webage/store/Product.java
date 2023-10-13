package com.webage.store;

public class Product {
	private String id;
	private String name;
	private String description;
	private double price;
	private String priceFormatted;
	private String imageURL;
	
	public Product() {
		
	}
	public Product(String id, String name, String description, double price,
			String priceFormatted, String imageURL) {
		super();
		this.id = id;
		this.name = name;
		this.description = description;
		this.price = price;
		this.priceFormatted = priceFormatted;
		this.imageURL = imageURL;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getDescription() {
		return description;
	}
	public void setDescription(String description) {
		this.description = description;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		this.price = price;
	}
	public String getPriceFormatted() {
		return priceFormatted;
	}
	public void setPriceFormatted(String priceFormatted) {
		this.priceFormatted = priceFormatted;
	}
	public String getImageURL() {
		return imageURL;
	}
	public void setImageURL(String imageURL) {
		this.imageURL = imageURL;
	}
}
